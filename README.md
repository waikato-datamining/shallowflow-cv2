# shallowflow-cv2
Imaging components using [OpenCV2](https://github.com/opencv/opencv-python) for shallowflow.

## Installation

Install via pip:

```bash
pip install "git+https://github.com/waikato-datamining/shallowflow-cv2.git"
```

## Actors

* Sources

  * ...
    
* Transformers

  * `shallowflow.cv2.transformers.ImageFileReader`
  * `shallowflow.cv2.transformers.VideoFileReader`
    
* Sinks

  * `shallowflow.cv2.sinks.ImageFileWriter`
  * `shallowflow.cv2.sinks.VideoFileWriter`

## Conversions

* `shallowflow.cv2.conversions.FrameToJpgBytes`
* `shallowflow.cv2.conversions.JpgBytesToFrame`

## Examples

* [extract video frames](examples/extract_video_frames.py)
