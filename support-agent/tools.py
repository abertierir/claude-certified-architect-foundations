""" Before you look at the reference solution below, write both definitions yourself in tools.py. You don't need to get them perfect, the point is to make deliberate choices so you have something concrete to compare against.

As you write get_customer, think about what Claude needs to know to use it correctly. What kinds of input might a customer give? What should Claude pass in? What does the tool return? And importantly — what should Claude do if it needs order details rather than customer details?

As you write lookup_order, think about what makes this tool distinct from get_customer in Claude's mind. They're both lookup tools. The description is what creates the separation. What does this tool specifically do that the other one doesn't? What does Claude need before it can use it?

Write your versions, then come back. """

""" tool = {
    "name": "get_customer",
    "description": "Plain English explanation of what this tool does",
    "input_schema": {
        "type": "object",
        "properties": {
            "param_name": {
                "type": "string",
                "description": "What this parameter is and what it accepts"
            }
        },
        "required": ["param_name"]
    }
}

customerTool = {
    "name": "get_customer",
   ## "description": "Some user don't know their IDs. With this service you can get as output the customer Id, and the information related to the personal information of the client. You are not going to receive information related to the customer orders.",
    "description": "USE this tool when:
- The user does not know their customer ID and needs it looked up
- You need to retrieve a customer's personal information (name, email, address, contact details, etc.)

DO NOT USE this tool when:
- You already have the customer ID and don't need additional personal info
- The user is asking about orders, purchases, or transaction history
- You need product, billing, or account activity data

OUTPUTS: customer_id, personal information (name, email, address, etc.)
DOES NOT OUTPUT: order history, purchases, or any transaction data",
    "input_schema": {
        "type": "object",
        "properties": {
            "param_name": {
                "type": "string",
                "description": "What this parameter is and what it accepts"
            }
        },
        "required": ["param_name"]
    }
}

orderTool = {
    "name": "lookup_order,",
   ## "description": "USE this tool when: Once you have customer ID and you need about orders, purchases, or transaction history. Get the orders by customer sending customer ID. As output you're going to get every order info",
    "description": "
USE this tool when:
- You have a customer ID and need to retrieve their order history
- The user is asking about past purchases or transactions

DO NOT USE this tool when:
- You don't have the customer ID yet (use the customer lookup tool first)
- The user is asking about personal information (name, email, address, etc.)
- The user is asking about product details or inventory

REQUIRES: customer_id
OUTPUTS: list of orders with order details (purchases, transactions, order history)
DOES NOT OUTPUT: personal information, product catalog, or inventory data
",
    "input_schema": {
        "type": "object",
        "properties": {
            "param_name": {
                "type": "string",
                "description": "What this parameter is and what it accepts"
            }
        },
        "required": ["param_name"]
    }
} """

tools = [
    {
        "name": "get_customer",
        "description": (
            "Look up a customer record by name, email address, or customer ID. "
            "Use this tool when you need to verify who you are speaking with or "
            "retrieve account information. Returns the customer's full profile "
            "including account status, contact details, and a list of their order IDs. "
            "Do not use this tool to look up order details — use lookup_order for that."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": (
                        "The search term to find the customer. Can be a full name "
                        "(e.g. 'Sarah Chen'), an email address (e.g. 'sarah@email.com'), "
                        "or a customer ID (e.g. 'CUST-4492')."
                    )
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "lookup_order",
        "description": (
            "Look up a specific order by order ID. Use this tool when you need "
            "details about a particular order — status, items, shipping information, "
            "estimated delivery dates, or notes. Requires a valid order ID. "
            "To find a customer's order IDs, call get_customer first."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": (
                        "The order ID to look up. Order IDs follow the format ORD-XXXX "
                        "(e.g. 'ORD-8821'). Must be an exact match."
                    )
                }
            },
            "required": ["order_id"]
        }
    }
]