import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const City: React.FC = () => {
  return (
    <div id="page-city-1">
    <div id="i6372" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="in7x5" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="inq8b" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="iuqln" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="igy3w" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/person">{"Person"}</a>
          <a id="iqbac" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/city">{"City"}</a>
        </div>
        <p id="ibaau" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="i6hi3" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="ie56i" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"City"}</h1>
        <p id="is0s1" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage City data"}</p>
        <TableBlock id="table-city-1" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="City List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Id", "column_type": "field", "field": "Id", "type": "str", "required": true}, {"label": "City", "column_type": "field", "field": "City", "type": "str", "required": true}], "formColumns": [{"column_type": "field", "field": "Id", "label": "Id", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "City", "label": "City", "type": "str", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "person", "field": "person", "lookup_field": "id", "entity": "Person", "type": "list", "required": false}]}} dataBinding={{"entity": "City", "endpoint": "/city/"}} />
      </main>
    </div>    </div>
  );
};

export default City;
