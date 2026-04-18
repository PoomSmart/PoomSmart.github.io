try:
	from .data_loader import load_category
except ImportError:
	from data_loader import load_category


youtube = load_category("youtube")
