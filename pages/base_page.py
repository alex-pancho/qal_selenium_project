from pages.elements import WebElement



class ItemProxy:
    def __init__(self, page):
        self.page = page

    def __getattr__(self, name: str) -> WebElement:
        _xpath = self.page.locators.get(name)
        if _xpath is None:
            msg = (
                f"{self.page.__class__.__name__} has no xpath "
                f"for element: {name}, "
                f"maybe typo? Existing names are: {list(self.page.locators.keys())}"
            )
            raise AttributeError(msg)
        return WebElement(driver=self.page.driver, xpath=_xpath)

    def __dir__(self):
        return list(self.page.locators.keys()) + super().__dir__()


class PageMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Збираємо всі атрибути-рядки як локатори
        locators = {}
        for key, value in namespace.items():
            if isinstance(value, str) and value.strip().startswith("//"):
                locators[key] = value

        # об’єднуємо з locators із батьків
        for base in bases:
            if hasattr(base, "locators"):
                locators = {**getattr(base, "locators"), **locators}

        namespace["locators"] = locators
        return super().__new__(mcs, name, bases, namespace)


class BasePage(metaclass=PageMeta):
    locators: dict[str, str] = {}
    URL = "https://automationexercise.com"

    def __init__(self, driver):
        self.driver = driver
        self.item = ItemProxy(self)
