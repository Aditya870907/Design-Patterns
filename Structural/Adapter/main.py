from payment import InHousePaymentProcessor, LegacyGateway, LegacyGatewayAdapter
from services.checkout_service import CheckoutService

class Main:
    def main():
        # Current Payment Processor
        processor = InHousePaymentProcessor()
        modern_checkout = CheckoutService(processor)
        print("\n--- Using Modern Payment Processor ---")
        modern_checkout.checkout(100, "Rupees")

        # Legacy Payment Processor
        legacy_gateway = LegacyGateway()
        legacy_adapter = LegacyGatewayAdapter(legacy_gateway)
        legacy_checkout = CheckoutService(legacy_adapter)
        print("\n--- Using Legacy Payment Processor ---")
        legacy_checkout.checkout(70, "Rupees")

if __name__ == "__main__":
    Main.main()