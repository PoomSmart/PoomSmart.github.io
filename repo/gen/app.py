try:
	from .data_loader import load_category
except ImportError:
	from data_loader import load_category


app = load_category("app")
