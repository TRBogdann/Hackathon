
import "./Row.scss"

function Row(props)
{return(
<>
<div class="row">
<div>{props.lat}</div>
<div>{props.lng}</div>
<div>{props.strada}</div>
<div>{props.tip}</div>
</div>
</>
);
}
export default Row;