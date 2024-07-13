from shiny import App, ui, render

class LengthConverter:
    """
    A class to convert lengths between different units with validation handled by Shiny.
    """
    def __init__(self):
        self.to_meters = {
            'inches': 0.0254, 'feet': 0.3048, 'yards': 0.9144,
            'meters': 1, 'centimeters': 0.01, 'millimeters': 0.001,
            'kilometers': 1000, 'miles': 1609.34, 'nautical miles': 1852
        }

    def convert(self, value, from_unit, to_unit):
        """
        Converts a value from one unit to another.
        """
        if value < 0:
            raise ValueError("Value must be non-negative.")
        if from_unit not in self.to_meters or to_unit not in self.to_meters:
            raise ValueError("Unsupported unit.")
        value_in_meters = value * self.to_meters[from_unit]
        converted_value = value_in_meters / self.to_meters[to_unit]
        return converted_value, from_unit, to_unit

# Unit options for the UI dropdown menus
unit_options = ['inches', 'feet', 'yards', 'meters', 'centimeters', 'millimeters', 'kilometers', 'miles', 'nautical miles']

# Define the UI layout
app_ui = ui.page_fluid(
    ui.panel_title("Length Unit Converter"),
    ui.panel_sidebar(
        ui.input_select("from_unit", "Convert from:", choices=unit_options),
        ui.input_select("to_unit", "Convert to:", choices=unit_options),
        ui.input_numeric("value", "Enter value:", value=1, min=0, step=0.01),
        ui.output_text("result")
    )
)

# Define the server logic
def server(input, output, session):
    converter = LengthConverter()

    @output
    @render.text
    def result():
        """
        Render the result of the conversion.
        """
        try:
            value = float(input.value())
            converted_value, from_unit, to_unit = converter.convert(value, input.from_unit(), input.to_unit())
            return f"{value} {from_unit} is {converted_value:.2f} {to_unit}."
        except ValueError as e:
            return str(e)

# Create the app
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
