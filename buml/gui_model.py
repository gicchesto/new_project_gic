####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
Person = Class(name="Person")
City = Class(name="City")

# Person class attributes and methods
Person_id: Property = Property(name="id", type=StringType)
Person_Person: Property = Property(name="Person", type=StringType)
Person_date_of: Property = Property(name="date_of", type=DateType)
Person.attributes={Person_Person, Person_date_of, Person_id}

# City class attributes and methods
City_Id: Property = Property(name="Id", type=StringType)
City_City: Property = Property(name="City", type=StringType)
City.attributes={City_City, City_Id}

# Relationships
inCity: BinaryAssociation = BinaryAssociation(
    name="inCity",
    ends={
        Property(name="person", type=Person, multiplicity=Multiplicity(0, 9999)),
        Property(name="city", type=City, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Person, City},
    associations={inCity},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="Person", view_elements=set(), is_main_page=True, route_path="/person", screen_size="Medium")
wrapper.component_id = "page-person-0"
i2nul = Text(
    name="i2nul",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i2nul",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i2nul"}
)
iqz5k = Link(
    name="iqz5k",
    description="Link element",
    label="Person",
    url="/person",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iqz5k",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/person", "id": "iqz5k"}
)
i29bl = Link(
    name="i29bl",
    description="Link element",
    label="City",
    url="/city",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i29bl",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/city", "id": "i29bl"}
)
ido3o = ViewContainer(
    name="ido3o",
    description=" component",
    view_elements={iqz5k, i29bl},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="ido3o",
    display_order=1,
    custom_attributes={"id": "ido3o"}
)
ido3o_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
ido3o.layout = ido3o_layout
i4kk5 = Text(
    name="i4kk5",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i4kk5",
    display_order=2,
    custom_attributes={"id": "i4kk5"}
)
ic9ss = ViewContainer(
    name="ic9ss",
    description="nav container",
    view_elements={i2nul, ido3o, i4kk5},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ic9ss",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ic9ss"}
)
ic9ss_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ic9ss.layout = ic9ss_layout
ip6li = Text(
    name="ip6li",
    content="Person",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ip6li",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ip6li"}
)
ip3ch = Text(
    name="ip3ch",
    content="Manage Person data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ip3ch",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ip3ch"}
)
table_person_0_col_0 = FieldColumn(label="Id", field=Person_id)
table_person_0_col_1 = FieldColumn(label="Person", field=Person_Person)
table_person_0_col_2 = FieldColumn(label="Date Of", field=Person_date_of)
table_person_0 = Table(
    name="table_person_0",
    title="Person List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_person_0_col_0, table_person_0_col_1, table_person_0_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-person-0",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Person List", "data-source": "0627952d-ad4c-44d2-a32c-03baeca15215", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'Person', 'label': 'Person', 'columnType': 'field', '_expanded': False}, {'field': 'date_of', 'label': 'Date Of', 'columnType': 'field', '_expanded': False}, {'field': 'City', 'label': 'City', 'columnType': 'lookup', 'lookupEntity': '3c4c6ca2-534b-472a-a05c-2b1a42fc3f5c', 'lookupField': 'Id', '_expanded': False}], "id": "table-person-0", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_person_0_binding_domain = None
if domain_model_ref is not None:
    table_person_0_binding_domain = domain_model_ref.get_class_by_name("Person")
if table_person_0_binding_domain:
    table_person_0_binding = DataBinding(domain_concept=table_person_0_binding_domain, name="PersonDataBinding")
else:
    # Domain class 'Person' not resolved; data binding skipped.
    table_person_0_binding = None
if table_person_0_binding:
    table_person_0.data_binding = table_person_0_binding
ii1x4 = ViewContainer(
    name="ii1x4",
    description="main container",
    view_elements={ip6li, ip3ch, table_person_0},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ii1x4",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ii1x4"}
)
ii1x4_layout = Layout(flex="1")
ii1x4.layout = ii1x4_layout
i7gqi = ViewContainer(
    name="i7gqi",
    description=" component",
    view_elements={ic9ss, ii1x4},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i7gqi",
    display_order=0,
    custom_attributes={"id": "i7gqi"}
)
i7gqi_layout = Layout(layout_type=LayoutType.FLEX)
i7gqi.layout = i7gqi_layout
wrapper.view_elements = {i7gqi}


# Screen: wrapper_2
wrapper_2 = Screen(name="wrapper_2", description="City", view_elements=set(), route_path="/city", screen_size="Medium")
wrapper_2.component_id = "page-city-1"
inq8b = Text(
    name="inq8b",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="inq8b",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "inq8b"}
)
igy3w = Link(
    name="igy3w",
    description="Link element",
    label="Person",
    url="/person",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="igy3w",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/person", "id": "igy3w"}
)
iqbac = Link(
    name="iqbac",
    description="Link element",
    label="City",
    url="/city",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iqbac",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/city", "id": "iqbac"}
)
iuqln = ViewContainer(
    name="iuqln",
    description=" component",
    view_elements={igy3w, iqbac},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iuqln",
    display_order=1,
    custom_attributes={"id": "iuqln"}
)
iuqln_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iuqln.layout = iuqln_layout
ibaau = Text(
    name="ibaau",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="ibaau",
    display_order=2,
    custom_attributes={"id": "ibaau"}
)
in7x5 = ViewContainer(
    name="in7x5",
    description="nav container",
    view_elements={inq8b, iuqln, ibaau},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="in7x5",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "in7x5"}
)
in7x5_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
in7x5.layout = in7x5_layout
ie56i = Text(
    name="ie56i",
    content="City",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ie56i",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ie56i"}
)
is0s1 = Text(
    name="is0s1",
    content="Manage City data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="is0s1",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "is0s1"}
)
table_city_1_col_0 = FieldColumn(label="Id", field=City_Id)
table_city_1_col_1 = FieldColumn(label="City", field=City_City)
table_city_1 = Table(
    name="table_city_1",
    title="City List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_city_1_col_0, table_city_1_col_1],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-city-1",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "City List", "data-source": "3c4c6ca2-534b-472a-a05c-2b1a42fc3f5c", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'Id', 'label': 'Id', 'columnType': 'field', '_expanded': False}, {'field': 'City', 'label': 'City', 'columnType': 'field', '_expanded': False}, {'field': 'Person', 'label': 'Person', 'columnType': 'lookup', 'lookupEntity': '0627952d-ad4c-44d2-a32c-03baeca15215', 'lookupField': 'id', '_expanded': False}], "id": "table-city-1", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_city_1_binding_domain = None
if domain_model_ref is not None:
    table_city_1_binding_domain = domain_model_ref.get_class_by_name("City")
if table_city_1_binding_domain:
    table_city_1_binding = DataBinding(domain_concept=table_city_1_binding_domain, name="CityDataBinding")
else:
    # Domain class 'City' not resolved; data binding skipped.
    table_city_1_binding = None
if table_city_1_binding:
    table_city_1.data_binding = table_city_1_binding
i6hi3 = ViewContainer(
    name="i6hi3",
    description="main container",
    view_elements={ie56i, is0s1, table_city_1},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i6hi3",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i6hi3"}
)
i6hi3_layout = Layout(flex="1")
i6hi3.layout = i6hi3_layout
i6372 = ViewContainer(
    name="i6372",
    description=" component",
    view_elements={in7x5, i6hi3},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i6372",
    display_order=0,
    custom_attributes={"id": "i6372"}
)
i6372_layout = Layout(layout_type=LayoutType.FLEX)
i6372.layout = i6372_layout
wrapper_2.view_elements = {i6372}

gui_module = Module(
    name="GUI_Module",
    screens={wrapper, wrapper_2}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
