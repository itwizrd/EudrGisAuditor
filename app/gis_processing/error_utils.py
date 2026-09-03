from pathlib import Path
import logging


logger = logging.getLogger(__name__)

class PathValidator:
    """Centralized path validation utility."""

    @staticmethod
    def validate_path(base_dir: Path, path_segment: str) -> Path:
        """Safely validates and resolves a path within a base directory."""
        base_dir = Path(base_dir).resolve()
        path = (base_dir / path_segment).resolve()
        if not path.is_relative_to(base_dir):
            raise ValueError("Invalid path segment")
        return path

    @staticmethod
    def ensure_directory_exists(path: Path) -> bool:
        """Ensures a directory exists, creates if necessary."""
        try:
            path.mkdir(parents=True, exist_ok=True)
            return True
        except OSError as e:
            logger.error(f"Failed to create directory {path}: {e}")
            return False

class DataValidator:
    """Data validation and sanitization utilities."""

    @staticmethod
    def create_empty_data_response() -> dict[str, object]:
        """Returns standardized empty data structure."""
        return {
            "summary_report_data": [],
            "detailed_report_data": [],
            "map_layers": [],
            "clean_file_count": 0
        }

    @staticmethod
    def validate_session_data(data: dict[str, object]) -> dict[str, object]:
        """Validates and sanitizes session data structure."""
        if not data or not isinstance(data, dict):
            return DataValidator.create_empty_data_response()

        validated = DataValidator.create_empty_data_response()

        if isinstance(data.get('summary_report_data'), list):
            validated['summary_report_data'] = data['summary_report_data']

        if isinstance(data.get('detailed_report_data'), list):
            validated['detailed_report_data'] = data['detailed_report_data']

        if isinstance(data.get('map_layers'), list):
            validated['map_layers'] = data['map_layers']

        if isinstance(data.get('clean_file_count'), int):
            validated['clean_file_count'] = data['clean_file_count']

        return validated

class ErrorHandler:
    """Centralized error handling utilities."""

    @staticmethod
    def handle_file_not_found(operation: str, path: str | None = None) -> dict[str, object]:
        """Standard response for file not found errors."""
        message = f"{operation} failed - file not found"
        if path:
            message += f": {path}"
        logger.warning(message)
        return {"error": "File not found", "data": DataValidator.create_empty_data_response()}

    @staticmethod
    def handle_processing_error(operation: str, error: Exception) -> dict[str, object]:
        """Standard response for processing errors."""
        message = f"{operation} failed: {str(error)}"
        logger.error(message, exc_info=True)
        return {"error": "Processing error", "data": DataValidator.create_empty_data_response()}

    @staticmethod
    def log_and_return_error(operation: str, error: Exception, include_data: bool = True) -> dict[str, object]:
        """Logs error and returns standardized error response."""
        logger.error(f"Error in {operation}: {error}", exc_info=True)
        response = {"error": str(error)}
        if include_data:
            response["data"] = DataValidator.create_empty_data_response()
        return response
