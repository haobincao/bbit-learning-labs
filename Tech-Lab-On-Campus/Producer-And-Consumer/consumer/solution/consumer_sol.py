

from consumer_interface import mqConsumerInterface


class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key, exchange_name, queue_name) -> None:
        super().__init__(binding_key, exchange_name, queue_name)

