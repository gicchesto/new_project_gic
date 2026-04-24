import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const Person: React.FC = () => {
  return (
    <div id="page-person-0">
    <div id="is13x" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="i8d4f" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="ih7xo" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="ivvd4" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="iy0ya" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/person">{"Person"}</a>
          <a id="i16pc" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/city">{"City"}</a>
        </div>
        <p id="iobgf" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="iypbf" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="ijaar" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Person"}</h1>
        <p id="ikb2n" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Person data"}</p>
        <TableBlock id="table-person-0" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Person List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Name", "column_type": "field", "field": "name", "type": "str", "required": true}, {"label": "Date Of", "column_type": "field", "field": "date_of", "type": "date", "required": true}], "formColumns": [{"column_type": "field", "field": "name", "label": "name", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "date_of", "label": "date_of", "type": "date", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "city", "field": "city", "lookup_field": "City", "entity": "City", "type": "str", "required": true}]}} dataBinding={{"entity": "Person", "endpoint": "/person/"}} />
      </main>
    </div>    </div>
  );
};

export default Person;
