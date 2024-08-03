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