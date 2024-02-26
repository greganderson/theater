from viewer import Viewer


class Theater:
    
    def __init__(self):
        # Make 10 rows
        self.num_rows = 10
        self.rows = [[] for _ in range(self.num_rows)]

        self.row_size = 20
        self.current_row = 1
    
    def add_viewer(self, viewer: Viewer) -> None:
        """ Adds a viewer to the theater, returning True if successful. If there are no seats left, return False. """
        # Add code here

        if len(self.rows[self.current_row - 1]) == self.row_size:
            if self.current_row == self.num_rows:
                return False
            self.current_row += 1

        self.rows[self.current_row - 1].append(viewer)
        return True
    
    def get_number_of_viewers(self) -> int:
        count = 0
        for row in self.rows:
            count += len(row)
        return count


def main():
    theater = Theater()

    viewers = [Viewer(f"Viewer {i}") for i in range(220)]

    for viewer in viewers:
        success = theater.add_viewer(viewer)
        if not success:
            print(f"Viewer {viewer.name} was denied entry")
    
    print(theater.get_number_of_viewers())


if __name__ == "__main__":
    main()