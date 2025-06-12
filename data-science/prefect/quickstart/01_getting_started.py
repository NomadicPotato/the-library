from prefect import flow, task
import random

@task #individual task decorator for prefect
def get_customer_ids() -> list[str]:
    # Fetch customer IDs from a database or API
    return [f"customer{n}" for n in random.choices(range(100), k=50)]

@task
def process_customer(customer_id: str) -> str:
    # Process a single customer
    return f"Processed {customer_id}"

# it should dynamically build the flow
@flow # flow decorator. this part of the code actual orchestrates the code
def main() -> list[str]:
    customer_ids = get_customer_ids()
    # Map the process_customer task across all customer IDs
    results = process_customer.map(customer_ids)
    return results


if __name__ == "__main__":
    main.serve(
        name="my-first-deployment", # added this to deploy it to the server?
        cron="*/5 * * * *"  # "0 8 * * *" Run every day at 8:00 AM, but modfied to run every 5 mins
    )
