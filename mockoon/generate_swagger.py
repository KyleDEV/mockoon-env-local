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
            # Assuming response body is a JSON object
            try:
                response_body = json.loads(response["body"])
            except json.JSONDecodeError:
                response_body = {}

            responses[str(response["statusCode"])] = {
                "description": response["label"],
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "example": response_body
                        }
                    }
                }
            }

        if path not in swagger["paths"]:
            swagger["paths"][path] = {}

        swagger["paths"][path][method] = {
            "summary": route["documentation"],
            "responses": responses
        }

    return swagger

with open('/usr/src/app/data/evergreen.json', 'r') as f:
    mockoon_data = json.load(f)

swagger_spec = generate_swagger(mockoon_data)

with open('/usr/src/app/swagger/swagger.json', 'w') as f:
    json.dump(swagger_spec, f, indent=2)
