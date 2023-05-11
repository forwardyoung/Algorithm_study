with recursive rc
as (
    select 0 as hour
    union all
    select hour+1
    from rc
    where hour<23
)

select rc.hour, count(hour(A.datetime)) as count
from rc left join animal_outs A
on rc.hour = hour(A.datetime) -- 재귀 숫자와 datetime 시간숫자가 같은것 만
group by rc.hour;