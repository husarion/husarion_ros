#include <ros/ros.h>
#include <std_msgs/Float32.h>
#include <sensor_msgs/Image.h>
#include <message_filters/subscriber.h>
#include <message_filters/synchronizer.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

ros::Publisher image_pub;
double binarized_max_val = 1;
double far_threshold_default = 2.5;
double far_threshold;
cv::Mat binarized;
cv::Mat color_cut;
cv::Mat far_mask;

void far_clipping_callback(const std_msgs::Float32 &clippingDistPtr)
{
  far_threshold = clippingDistPtr.data;
}

void callback(const sensor_msgs::ImageConstPtr &rgb, const sensor_msgs::ImageConstPtr &depth)
{
  try
  {
    cv_bridge::CvImagePtr cv_ptr_rgb = cv_bridge::toCvCopy(rgb, sensor_msgs::image_encodings::BGR8);
    cv_bridge::CvImagePtr cv_ptr_depth = cv_bridge::toCvCopy(depth, sensor_msgs::image_encodings::TYPE_32FC1);
    threshold(cv_ptr_depth->image, binarized, far_threshold, binarized_max_val, cv::ThresholdTypes::THRESH_BINARY_INV);
    binarized.convertTo(far_mask, CV_8UC1, binarized_max_val);
    bitwise_and(cv_ptr_rgb->image, cv_ptr_rgb->image, color_cut, far_mask);
    cv_ptr_rgb->image = color_cut;
    image_pub.publish(cv_ptr_rgb->toImageMsg());
    binarized.release();
    color_cut.release();
    far_mask.release();
  }
  catch (cv_bridge::Exception &e)
  {
    ROS_ERROR("cv_bridge exception: %s", e.what());
    return;
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "clipping_node");
  ros::NodeHandle nh("~");
  nh.param<double>("clipping_distance", far_threshold, far_threshold_default);
  message_filters::Subscriber<sensor_msgs::Image> image_rgb_sub(nh, "/camera/rgb/image_raw", 1);
  message_filters::Subscriber<sensor_msgs::Image> image_depth_sub(nh, "/camera/depth/image", 1);
  ros::Subscriber clipping_distance_sub = nh.subscribe("/clipping/distance", 1, far_clipping_callback);

  typedef message_filters::sync_policies::ApproximateTime<sensor_msgs::Image, sensor_msgs::Image> MySyncPolicy;
  message_filters::Synchronizer<MySyncPolicy> sync(MySyncPolicy(10), image_rgb_sub, image_depth_sub);
  image_pub = nh.advertise<sensor_msgs::Image>("/clipping/output", 1);
  sync.registerCallback(boost::bind(&callback, _1, _2));
  ros::spin();
  return 0;
}