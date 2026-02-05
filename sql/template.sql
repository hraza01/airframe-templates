-- Template SQL that uses API response data from call_external_api task
-- The api_response is passed via params and contains the API call result

SELECT STRUCT(
  {{ params.api_response.data.userId }} AS user_id,
  {{ params.api_response.data.id }} AS id,
  '{{ params.api_response.data.title }}' AS title,
  '{{ params.api_response.data.body }}' AS body
) AS response
