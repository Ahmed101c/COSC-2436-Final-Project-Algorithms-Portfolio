class Box:
    def __init__(self, label: str, length: float, width: float, height: float):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        """Calculate the volume of the box."""
        return self.length * self.width * self.height


def pack_truck(boxes: list, truck_volume: float) -> list:
    """Pack the truck using a greedy strategy based on box volumes."""
    # Sort boxes in descending order of volume
    boxes_sorted = sorted(boxes, key=lambda box: box.volume(), reverse=True)

    packed_boxes = []
    used_volume = 0

    for box in boxes_sorted:
        if used_volume + box.volume() <= truck_volume:
            packed_boxes.append(box)
            used_volume += box.volume()

    return packed_boxes


if __name__ == "__main__":
    print("Welcome to the Truck Cargo Calculator")
    print("This program helps you calculate how to pack your cargo efficiently using a greedy algorithm.\n")

    # Input truck dimensions
    length = float(input("Enter truck length: "))
    width = float(input("Enter truck width: "))
    height = float(input("Enter truck height: "))

    truck_volume = length * width * height
    print(f"Truck Volume: {truck_volume}\n")

    boxes = []

    # Input boxes
    while True:
        label = input("Enter box label (or 'done' to finish): ")
        if label.lower() == "done":
            break

        length = float(input("Enter box length: "))
        width = float(input("Enter box width: "))
        height = float(input("Enter box height: "))

        box = Box(label, length, width, height)
        boxes.append(box)

    # Pack truck
    packed_boxes = pack_truck(boxes, truck_volume)

    # Display results
    total_used_volume = sum(box.volume() for box in packed_boxes)

    print("\nPacked Boxes:")
    for box in packed_boxes:
        print(f"{box.label} (Volume: {box.volume()})")

    print(f"\nTotal Used Volume: {total_used_volume}")
    print(f"Remaining Volume: {truck_volume - total_used_volume}")

    print("\nThank you for using the Truck Cargo Calculator.")
