import cv2
import numpy
from shallowflow.api.sink import AbstractFileWriter


class ImageFileWriter(AbstractFileWriter):
    """
    Writes the incoming image data to disk.
    """

    def description(self):
        """
        Returns a description for the actor.

        :return: the actor description
        :rtype: str
        """
        return "Writes the incoming image data to disk."

    def accepts(self):
        """
        Returns the types that are accepted.

        :return: the list of types
        :rtype: list
        """
        return [numpy.ndarray, bytes]

    def _do_execute(self):
        """
        Performs the actual execution.

        :return: None if successful, otherwise error message
        :rtype: str
        """
        result = None
        output_path = self.variables.expand(self.get("output_file"))
        try:
            if isinstance(self._input, bytes):
                with open(output_path, "wb") as fp:
                    fp.write(self._input)
            else:
                cv2.imwrite(output_path, self._input)
        except Exception:
            result = self._handle_exception("Failed to write image to %s" % output_path)
        return result
