import socket

from confluent_kafka import Producer


class SolarPlateProducer:
    def __init__(
        self,
    ) -> None:
        conf = {
            "bootstrap.servers": "kafka:9092",
            "client.id": socket.gethostname(),
        }

        self.producer = Producer(conf)

    def produce(
        self,
    ):
        producer_data = {
            "event_date": "2023-07-20T14:12:37.723919",
            "power_delivery": 10.1,
            "solar_plate_id": "b616183e-584a-41fa-9355-9f8b57003275",
        }
        self.producer.produce("solar-plate", key="key", value=str(producer_data))
        self.producer.flush()


if __name__ == "__main__":
    producer = SolarPlateProducer()
    producer.produce()
