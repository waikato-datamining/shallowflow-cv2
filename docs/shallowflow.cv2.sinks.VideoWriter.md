# VideoWriter

## Name
shallowflow.cv2.sinks.VideoWriter

## Synopsis
Writes the incoming image data to disk as MJPEG video.

## Flow input/output
input: numpy.ndarray, builtins.bytes

## Options
* debug (bool)

  * If enabled, outputs some debugging information
  * default: False

* skip (bool)

  * Whether to skip this actor during execution
  * default: False

* annotation (str)

  * For adding documentation to the actor
  * default: ''

* name (str)

  * The name to use for this actor, leave empty for class name
  * default: ''

* stop_flow_on_error (bool)

  * Whether to stop the flow in case of an error
  * default: True

* output_file (File)

  * The file to write to; can contain variables; use .avi or .mkv as extension.
  * default: '.'

* fps (float)

  * The frames-per-second to use in the output video.
  * default: 30.0

