from taipy.gui import Gui, notify, State
from taipy import Config, Core, Scope
import pandas as pd

class WorkspaceUI:
    def __init__(self, metadata):
        self.metadata = metadata
        self.tables = list(metadata.keys())
        self.selected_table = None
        self.columns = []
        self.mappings = {}

    def on_table_select(self, state, table):
        state.selected_table = table
        state.columns = list(self.metadata[table].keys())

    def on_create_mapping(self, state):
        if state.selected_table and state.selected_column:
            if state.selected_table not in self.mappings:
                self.mappings[state.selected_table] = {}
            self.mappings[state.selected_table][state.selected_column] = state.target_column
            notify(state, "success", f"Mapping created: {state.selected_table}.{state.selected_column} -> {state.target_column}")
        else:
            notify(state, "error", "Please select a table and a column")

    def get_mappings(self):
        return self.mappings

    def run(self):
        page = """
        <|layout|columns=1 1|
        <|
        Tables:
        <|{tables}|selector|lov={tables}|on_change=on_table_select|>

        Columns:
        <|{columns}|selector|lov={columns}|>
        |>

        <|
        Target Column: <|{target_column}|input|>
        <|Create Mapping|button|on_action=on_create_mapping|>
        |>
        |>

        Current Mappings:
        <|{pd.DataFrame(mappings).to_html()}|raw|>
        """

        variables = {
            "tables": self.tables,
            "columns": self.columns,
            "selected_table": self.selected_table,
            "target_column": "",
            "mappings": self.mappings
        }

        Gui(page).run(data=variables)
