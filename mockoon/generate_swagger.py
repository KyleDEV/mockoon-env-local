import json

def generate_swagger(mockoon_data):
    swagger = {
        "openapi": "3.0.0",
        "info": {
            "title": mockoon_data.get("name", "API"),
            "version": "1.0.0"
        },
        "paths": {}
    }

    for route in mockoon_data["routes"]:
        path = f"/api/{route['endpoint']}"
        method = route['method']
        responses = {}

        for response in route["responses"]:
            # Assuming response body is a JSON object or faker template
            try:
                response_body = json.loads(response["body"])
            except json.JSONDecodeError:
                response_body = response["body"]  # Keeping the body as string if not JSON

            # Creating the response content schema
            if isinstance(response_body, dict):
                schema = {
                    "type": "object",
                    "example": response_body
                }
            else:
                schema = {
                    "type": "string",
                    "example": response_body
                }

            responses[str(response["statusCode"])] = {
                "description": response["label"],
                "content": {
                    "application/json": {
                        "schema": schema
                    }
                }
            }

        if path not in swagger["paths"]:
            swagger["paths"][path] = {}

        swagger["paths"][path][method] = {
            "summary": route["documentation"],
            "responses": responses
        }

        # Add request body if available
        if route["responses"]:
            request_body = {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object"
                        }
                    }
                }
            }
            swagger["paths"][path][method]["requestBody"] = request_body

    return swagger

with open('/usr/src/app/data/evergreen.json', 'r') as f:
    mockoon_data = json.load(f)

swagger_spec = generate_swagger(mockoon_data)

with open('/usr/src/app/swagger/swagger.json', 'w') as f:
    json.dump(swagger_spec, f, indent=2)
