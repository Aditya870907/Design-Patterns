from vending_machine import VendingMachine
def main():
    vm = VendingMachine()

    vm.insert_coin(1.0)
    vm.dispense_item()
    vm.select_item("A1")
    vm.insert_coin(1.0)
    vm.dispense_item()

    print("\n Second Transation")
    vm.select_item("A2")
    vm.dispense_item()
    vm.insert_coin(1.5)
    vm.dispense_item()

if __name__ == "__main__":
    main()