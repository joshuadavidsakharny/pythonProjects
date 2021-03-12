# python program using instance of EasyFrame to simulate simple application
# which displays ticket pricing along with discount
# allows user to input age, prints discount, and prints discounted total

from breezypythongui import EasyFrame


class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)

        # title and description labels
        self.label = self.addLabel(text="Ticket Discount Calculator",
                                   row=0, column=0,
                                   columnspan=2, sticky="NSEW")
        self.label2 = self.addLabel(text="Original Ticket Price = $25.00",
                                    row=1, column=0,
                                    columnspan=2, sticky="NSEW")
        self.label3 = self.addLabel(text="Children (16 & Younger) = 10% Discount",
                                    row=2, column=0,
                                    columnspan=2, sticky="W")
        self.label4 = self.addLabel(text="Adults (17 - 64) = 2% (of Age) Discount",
                                    row=3, column=0,
                                    columnspan=2, sticky="W")
        self.label5 = self.addLabel(text="Seniors (65 & Older) = 20% Discount",
                                    row=4, column=0,
                                    columnspan=2, sticky="W")

        # clears all field entries for re-use of program / gui
        self.clearBtn = self.addButton(text="Clear",
                                       row=5, column=0,
                                       command=self.clear)

        # Label and field for the input (age)
        self.addLabel(text="Input Age",
                      row=6, column=0)
        self.inputField = self.addTextField(text="",
                                            row=6,
                                            column=1)
        # Label and field for the discount section
        self.addLabel(text="Discount",
                      row=7, column=0)
        self.outputField = self.addTextField(text="",
                                             row=7,
                                             column=1,
                                             state="readonly")
        # label and field for the discounted total section
        self.addLabel(text="Discounted Total",
                      row=8, column=0)
        self.outputField2 = self.addTextField(text="",
                                              row=8,
                                              column=1,
                                              state="readonly")

        # command button / calculates discount and discounted totals
        self.button = self.addButton(text="Calculate Discount",
                                     row=5, column=1,
                                     columnspan=2,
                                     command=self.calculate)

    # event handling method for the button
    def calculate(self):
        """."""
        int1 = self.inputField.getText()
        age = int(int1)
        discount = int(0)
        total = int(25)

        # comparison operations to determine discount per age limits
        if 16 < age < 65:
            discount += age * .02
        elif age >= 65:
            discount += 25 * .20
        elif age <= 16:
            discount = 25 * .10

        self.outputField.setText("- $" + str(format(discount, '.2f')))
        self.outputField2.setText("$" + str(format(total - discount, '.2f')))

    # methods to handle user events
    def clear(self):
        """Resets the label to the empty string and
        the button states."""
        self.inputField.setValue("")
        self.outputField.setValue("")
        self.outputField2.setValue("")


# instantiates and pops up the window
if __name__ == "__main__":
    ButtonDemo().mainloop()
