import cv2
import numpy
from coed.config import Option
from shallowflow.api.transformer import AbstractSimpleTransformer
from shallowflow.api.io import File
from ._image_output import IMAGE_OUTPUTS, IMAGE_OUTPUT_NUMPY, IMAGE_OUTPUT_PNG, IMAGE_OUTPUT_JPG


class ImageFileReader(AbstractSimpleTransformer):
    """
    Loads the image.
    """

    def description(self):
        """
        Returns a description for the actor.

        :return: the actor description
        :rtype: str
        """
        return "Loads the image."

    def _define_options(self):
        """
        For configuring the options.
        """
        super()._define_options()
        self._option_manager.add(Option(name="image_output", value_type=str, def_value=IMAGE_OUTPUT_NUMPY, choices=IMAGE_OUTPUTS,
                                        help="In what format to forward the image."))

    def accepts(self):
        """
        Returns the types that are accepted.

        :return: the list of types
        :rtype: list
        """
        return [File]

    def generates(self):
        """
        Returns the types that get generated.

        :return: the list of types
        :rtype: list
        """
        if self.get("image_output") == IMAGE_OUTPUT_NUMPY:
            return [numpy.ndarray]
        elif self.get("image_output") in [IMAGE_OUTPUT_JPG, IMAGE_OUTPUT_PNG]:
            return [bytes]
        else:
            raise Exception("Unhandled image output: %s" % str(self.get("image_output")))

    def _do_execute(self):
        """
        Performs the actual execution.

        :return: None if successful, otherwise error message
        :rtype: str
        """
        result = None
        try:
            self._output.append(cv2.imread(self._input))
        except Exception:
            result = self._handle_exception("Failed to open image file: %s" % str(self._input))
        return result
