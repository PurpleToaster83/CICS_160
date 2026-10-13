class Model_List:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_item_n(self, n):
        if n >= len(self):
            n = -1

        return self.items[n]

class View_List:
    def show_items(slef, items):
        print("\n***Gocercy List***")

        if not items:
            print("No Items Please Add some")
        else:
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")

    def get_user_input(self):
        return input("\nEnter a new item (or 'q' to quit): ")

class Controller_List:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self, item):
        item = item.strip().capitalize() #clean
        self.model.add_item(item)

    def display_view(self):
        items = self.model.get_items()
        self.view.show_items(items)

    def run(self):
        while True:
            self.display_view()
            i = self.view.get_user_input()
            if i.lower() in ['q', 'quit','end','done','']:
                return
            self.add_item(i)

if __name__ == "__main__":
    model = Model_List()
    view = View_List()
    controller = Controller_List(model, view)

    controller.run()