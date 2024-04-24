# ImageFileReader

## Name
shallowflow.cv2.transformers.ImageFileReader

## Synopsis
Loads the image.

## Flow input/output
input: shallowflow.api.io.File

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

* image_output (str)

  * In what format to forward the image.
  * default: 'numpy'
  * choices: ['numpy', 'jpg', 'png']

