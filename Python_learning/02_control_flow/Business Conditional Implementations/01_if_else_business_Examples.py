## Order status Calculation
"""
PENDING    → Order is waiting for processing
CONFIRMED  → Order is confirmed
SHIPPED    → Order is in transit
DELIVERED  → Order completed successfully
CANCELLED  → Order was cancelled
anything else → Unknown order status

"""
order = {
    "order_id": 1001,
    "status": "SHIPPED"
}

if order["status"] == "PENDING":
    print(f"Order {order['order_id']} is waiting for processing ")
elif order["status"]=="CONFIRMED":
    print(f"Order {order['order_id']} is confirmed ")
elif order["status"]=="SHIPPED":
    print(f"Order {order['order_id']} Order is in transit ")
elif order["status"]=="DELIVERED":
    print(f"Order {order['order_id']} completed successfully ")
elif order["status"]=="CANCELLED":
    print(f"Order {order['order_id']} was cancelled")
else:
    print("Unknown order status")


## Customer Category

customer = {
    "customer_id": 501,
    "total_spent": 75000
}

"""
total_spent >= 100000
        ↓
Premium

total_spent >= 50000
        ↓
Gold

total_spent >= 10000
        ↓
Silver

below 10000
        ↓
Standard
"""

if customer["total_spent"] >= 100000:
    print(f"Premium Customer {customer['customer_id']}")
elif customer["total_spent"] >= 50000:
    print(f"Gold Customer {customer['customer_id']}")
elif customer["total_spent"] >= 10000:
    print(f"Silver Customer {customer['customer_id']}")
else:
    print(f"Standard Customer {customer['customer_id']}")


## 3. Transaction Status
transaction = {
    "transaction_id": "TXN1001",
    "status": "FAILED",
    "amount": 25000,
    "retry_count": 1
}

"""
SUCCESS
   ↓
Transaction completed

FAILED + retry_count < 3
   ↓
Retry transaction

FAILED + retry_count >= 3
   ↓
Escalate transaction

PENDING
   ↓
Wait for transaction completion

anything else
   ↓
Unknown transaction status
"""

if transaction["status"] == "SUCCESS":
    print(f"{transaction['transaction_id']} Transaction completed")

elif transaction["status"] == "FAILED" and transaction["retry_count"] < 3:
    print(f"Retry transaction {transaction['transaction_id']}")

elif transaction["status"] == "FAILED":
    print(f"Escalate transaction {transaction['transaction_id']}")

elif transaction["status"] == "PENDING":
    print(f"Wait for transaction completion {transaction['transaction_id']}")

else:
    print("Unknown transaction status")


#4 Pipeline Status

pipeline = {
    "name": "daily_sales_etl",
    "status": "FAILED",
    "retry_count": 2,
    "processed_records": 1500
}

'''
SUCCESS
   ↓
Pipeline completed

FAILED + retry_count < 3
   ↓
Retry pipeline

FAILED + retry_count >= 3
   ↓
Escalate to operations

RUNNING + processed_records > 0
   ↓
Pipeline is actively processing

RUNNING + processed_records == 0
   ↓
Pipeline may be stuck

anything else
   ↓
Monitor / investigate
'''

if pipeline["status"] == "SUCCESS":
    print(f"{pipeline['name']} completed successfully")

elif pipeline["status"] == "FAILED" and pipeline["retry_count"] < 3:
    print(f"{pipeline['name']} retry pipeline")

elif pipeline["status"] == "FAILED":
    print(
        f"Escalate to operations with respect to pipeline: "
        f"{pipeline['name']}"
    )

elif pipeline["status"] == "RUNNING" and pipeline["processed_records"] > 0:
    print(f"{pipeline['name']} is processing records")

elif pipeline["status"] == "RUNNING":
    print(f"{pipeline['name']} may be stuck")

else:
    print("Monitor / investigate")


