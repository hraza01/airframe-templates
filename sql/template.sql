{% set api_response = task_instance.xcom_pull(task_ids=params.upstream_task_id) %}

select struct(
           {{ api_response.data.userId }} as user_id,
           {{ api_response.data.id }} as id,
           '{{ api_response.data.title | replace("\n", " ") }}' as title,
           '{{ api_response.data.body | replace("\n", " ") }}' as body
       ) as response
     , '{{ api_response.message }}' as message
     , '{{ api_response.status }}' as status
     , '{{ api_response.status_code }}' as status_code