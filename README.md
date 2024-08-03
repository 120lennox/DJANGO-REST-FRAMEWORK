# Django Rest Framework study notes
#### https://www.django-rest-framework.org/api-guide/routers/

## Tutorial 2
#### https://www.django-rest-framework.org/tutorial/2-requests-and-responses/

Tutorial 2 introduces two objects essential for working with web APIs. These include **Request Objects** and **Response Objects**

### Request Objects
- A Request object is an extension from HttpRequest object.
- Request object handles all requests from client. 
- Has features like;
  - **request.data** which gives access to the submitted data (works for POST, PUT, PATCH)
  - **request.query_params**: Provides access to query parameters in the URL
  - **request.method**: Tells you which HTTP method was used (GET, POST, etc.)
  - **request.user**: Gives information about the authenticated user (if any)

### Response Objects
The Response object in Django Rest Framework (DRF) is the counterpart to the Request object.

A Response object is what your DRF views return. It's a way to send data back to the client along with other important information about the response.

What it does:
1. Carries data: It holds the data you want to send back to the client.
2. Sets metadata: It allows you to set status codes, headers, and content types.
3. Handles serialization: It can automatically convert Python data types to JSON or other formats.

Key features:
- Can be initialized with data, status, and headers
- Automatically sets the content type (usually to JSON)
- Works with DRF's content negotiation to return data in the format the client expects

Basic usage:
```python
from rest_framework.response import Response

def my_view(request):
    data = {'message': 'Hello, World!'}
    return Response(data)
```

This will automatically serialize the data to JSON and set the appropriate content type.

You can also set status codes:
```python
return Response(data, status=status.HTTP_201_CREATED)
```

The Response object simplifies the process of sending data back to the client in a format that follows REST conventions.
