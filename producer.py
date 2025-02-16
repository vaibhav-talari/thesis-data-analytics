import csv
import json
from kafka import KafkaProducer

# Kafka configuration
KAFKA_BROKER = 'localhost:9092'  # Change this to your Kafka broker
KAFKA_TOPIC = 'quickstart-events'  # Change this to your Kafka topic

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def read_csv_and_produce(csv_file):
    """ Reads a CSV file and pushes each row as a message to Kafka. """
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            producer.send(KAFKA_TOPIC, value=row)
            print(f'Message sent: {row}')
    producer.flush()  # Ensure all messages are sent

if __name__ == "__main__":
    csv_file_path = 'data/generated_event_with_deviations.csv'  # Change this to your CSV file path
    read_csv_and_produce(csv_file_path)
