# python program using instance of EasyFrame to simulate simple application
# which allows user to calculate airplane climb rate
# asks for:
# ::: input of obstruction height
# ::: distance from obstruction to airplane takeoff
# ::: and airplane ground speed
# calculates and displays recommended climb rate
# displays actual altitude of airplane at moment of obstruction over-fly

from breezypythongui import EasyFrame


class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)

        # title and description labels
        self.label = self.addLabel(text="Airplane Climb Rate Calculator",
                                   row=0, column=0,
                                   columnspan=2, sticky="NSEW")

        # clears all field entries for re-use of program / gui
        self.clearBtn = self.addButton(text="Clear",
                                       row=1, column=0,
                                       command=self.clear)

        # label and text field for obstruction height in meters
        # ::: INPUT
        self.addLabel(text="Obstruction Height (m)",
                      row=2, column=0)
        self.inputField = self.addTextField(text="",
                                            row=2,
                                            column=1)
        # label and text field for obstruction to lift-off distance in meters
        # ::: INPUT
        self.addLabel(text="Obstruction To Lift-Off Distance (m)",
                      row=3, column=0)
        self.inputField2 = self.addTextField(text="",
                                             row=3,
                                             column=1)
        # label and text field for ground speed in kilometers per hour
        # ::: INPUT
        self.addLabel(text="Ground Speed (km/h)",
                      row=4, column=0)
        self.inputField3 = self.addTextField(text="",
                                             row=4,
                                             column=1)

        # label and text field for recommended climb rate in m/km per hour
        # ::: OUTPUT
        self.addLabel(text="Recommended Climb Rate (km^2/h)",
                      row=5, column=0)
        self.outputField = self.addTextField(text="",
                                             row=5,
                                             column=1,
                                             state="readonly")

        # label and text field for recommended climb rate in m/km per hour
        # ::: OUTPUT
        self.addLabel(text="Obstruction Over-Fly Altitude",
                      row=6, column=0)
        self.outputField2 = self.addTextField(text="",
                                              row=6,
                                              column=1,
                                              state="readonly")

        # command button / calculates discount and discounted totals
        self.button = self.addButton(text="Calculate Climb Rate",
                                     row=1, column=1,
                                     columnspan=2,
                                     command=self.calculate)

    # event handling method for the button
    def calculate(self):
        obstr_h = float(self.inputField.getText())
        obstr_lift_d = float(self.inputField2.getText())
        ground_speed = float(self.inputField3.getText())

        re_t = 0
        re_t += obstr_lift_d / ground_speed
        # m/

        re_climb_r = 0
        re_climb_r += (obstr_h + 2) / obstr_lift_d
        #

        self.outputField.setText(str(re_climb_r * re_t) + " km^2/h")
        self.outputField2.setText(str(obstr_h + 2) + " m")

    # methods to handle user events
    # ::: CLEAR
    def clear(self):
        """Resets the label to the empty string and
        the button states."""
        self.inputField.setValue("")
        self.inputField2.setValue("")
        self.inputField3.setValue("")
        self.outputField.setValue("")
        self.outputField2.setValue("")


# instantiates and pops up the window
if __name__ == "__main__":
    ButtonDemo().mainloop()
