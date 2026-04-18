try:
	from .data_loader import load_category
except ImportError:
	from data_loader import load_category


emoji = load_category("emoji")
