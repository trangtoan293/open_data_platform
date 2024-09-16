class DataMapping:
    def __init__(self, source_metadata, target_metadata):
        self.source_metadata = source_metadata
        self.target_metadata = target_metadata
        self.mappings = {}

    def add_mapping(self, source_table, target_table, column_mappings):
        if source_table not in self.mappings:
            self.mappings[source_table] = {}
        self.mappings[source_table][target_table] = column_mappings

    def get_mappings(self):
        return self.mappings