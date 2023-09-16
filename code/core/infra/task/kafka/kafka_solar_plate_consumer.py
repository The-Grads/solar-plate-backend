import json

from core.domain.entity.power_data import PowerData
from core.infra.factory.power_service_data_factory import PowerDataServiceFactory

from .base_consumer import KafkaConsumer


class SolarPlateConsumer(KafkaConsumer):
    def __init__(
        self,
    ) -> None:
        super().__init__(topic_list=["solar-plate"])
        self.power_data_service = PowerDataServiceFactory().create()

    def consume(
        self,
    ):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    print("Waiting...")
                elif msg.error():
                    print("ERROR: ", msg.error())
                else:
                    print(
                        f"Consumed event from topic {msg.topic()}: key = {msg.key()} value = {msg.value()}"
                    )
                    data = json.loads(msg.value().decode("utf8").replace("'", '"'))
                    power_data = PowerData(
                        solar_plate_id=data["solar_plate_id"],
                        power_delivery=data["power_delivery"],
                        event_date=data["event_date"],
                    )
                    self.power_data_service.create(power_data)

        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()
