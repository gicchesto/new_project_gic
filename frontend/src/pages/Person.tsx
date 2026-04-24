import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const Person: React.FC = () => {
  return (
    <div id="page-person-0">
    <div id="i7gqi" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="ic9ss" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="i2nul" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="ido3o" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="iqz5k" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/person">{"Person"}</a>
          <a id="i29bl" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/city">{"City"}</a>
        </div>
        <p id="i4kk5" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="ii1x4" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="ip6li" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Person"}</h1>
        <p id="ip3ch" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Person data"}</p>
        <TableBlock id="table-person-0" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Person List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Id", "column_type": "field", "field": "id", "type": "str", "required": true}, {"label": "Person", "column_type": "field", "field": "Person", "type": "str", "required": true}, {"label": "Date Of", "column_type": "field", "field": "date_of", "type": "date", "required": true}], "formColumns": [{"column_type": "field", "field": "id", "label": "id", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "Person", "label": "Person", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "date_of", "label": "date_of", "type": "date", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "city", "field": "city", "lookup_field": "Id", "entity": "City", "type": "str", "required": true}]}} dataBinding={{"entity": "Person", "endpoint": "/person/"}} />
      </main>
    </div>    </div>
  );
};

export default Person;
