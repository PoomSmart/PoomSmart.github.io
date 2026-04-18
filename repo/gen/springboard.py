try:
	from .data_loader import load_category
except ImportError:
	from data_loader import load_category


springboard = load_category("springboard")
