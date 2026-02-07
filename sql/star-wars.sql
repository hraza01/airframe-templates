{%- import 'sql/templates/_partial.sql' as p -%}
{%- set characters = [
        "Obi-Wan Kenobi",
        "Qui-Gon Jinn",
        "Yoda",
        "Darth Vader",
        "Han Solo",
    ] 
-%}

with base_query as (

    {%- for char in characters %}
   
    select "{{ char }}" as character_name

     union all 

    {%- endfor %}

    {{ p.my_partial() }}

)

select character_name
  from base_query;
