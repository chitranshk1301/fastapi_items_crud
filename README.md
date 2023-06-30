# FastAPI E-commerce CRUD

This is a simple e-commerce application built with FastAPI.

## Features

- CRUD routes for item manipulation
- API to add to inventory

## Prerequisites

- Python 3.7 or above
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [pydantic](https://pydantic-docs.helpmanual.io/)

## Getting Started

1. Clone the repository:
    
    ```bash
    git clone git@github.com:chitranshk1301/fastapi_items_crud.git
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:

    ```bash
    uvicorn main:app --reload
    ```

4. Navigate to [http://localhost:8000/docs] to view the Swagger UI.

## API Endpoints

#### Items

- `GET /items` - Returns a list of all items.
- `GET /items/{item_id}` - Returns a single item with the given ID.
- `POST /items` - Creates a new item.
- `PUT /items/{item_id}` - Updates an item with the given ID.
- `DELETE /items/{item_id}` - Deletes an item with the given ID.


