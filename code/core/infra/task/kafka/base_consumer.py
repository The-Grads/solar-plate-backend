from typing import Dict, List

from confluent_kafka import Consumer


class KafkaConsumer:
    consumer: Consumer

    def __init__(
        self,
        topic_list: List[str],
        conf_dict: Dict = None,
    ) -> None:
        if conf_dict is None:
            conf_dict = {
                "bootstrap.servers": "kafka:9092",
                "group.id": "counting-group",
                "enable.auto.commit": True,
                "session.timeout.ms": 6000,
                "default.topic.config": {"auto.offset.reset": "smallest"},
            }

        self.__topic_list = topic_list
        self.__conf_dict = conf_dict

        self.consumer = Consumer(self.__conf_dict)
        self.consumer.subscribe(self.__topic_list)
