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
Person_name: Property = Property(name="name", type=StringType)
Person_date_of: Property = Property(name="date_of", type=DateType)
Person.attributes={Person_date_of, Person_name}

# City class attributes and methods
City_City: Property = Property(name="City", type=StringType)
City.attributes={City_City}

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
ih7xo = Text(
    name="ih7xo",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ih7xo",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ih7xo"}
)
iy0ya = Link(
    name="iy0ya",
    description="Link element",
    label="Person",
    url="/person",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iy0ya",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/person", "id": "iy0ya"}
)
i16pc = Link(
    name="i16pc",
    description="Link element",
    label="City",
    url="/city",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i16pc",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/city", "id": "i16pc"}
)
ivvd4 = ViewContainer(
    name="ivvd4",
    description=" component",
    view_elements={iy0ya, i16pc},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="ivvd4",
    display_order=1,
    custom_attributes={"id": "ivvd4"}
)
ivvd4_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
ivvd4.layout = ivvd4_layout
iobgf = Text(
    name="iobgf",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="iobgf",
    display_order=2,
    custom_attributes={"id": "iobgf"}
)
i8d4f = ViewContainer(
    name="i8d4f",
    description="nav container",
    view_elements={ih7xo, ivvd4, iobgf},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i8d4f",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i8d4f"}
)
i8d4f_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i8d4f.layout = i8d4f_layout
ijaar = Text(
    name="ijaar",
    content="Person",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ijaar",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ijaar"}
)
ikb2n = Text(
    name="ikb2n",
    content="Manage Person data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ikb2n",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ikb2n"}
)
table_person_0_col_0 = FieldColumn(label="Name", field=Person_name)
table_person_0_col_1 = FieldColumn(label="Date Of", field=Person_date_of)
table_person_0 = Table(
    name="table_person_0",
    title="Person List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_person_0_col_0, table_person_0_col_1],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-person-0",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Person List", "data-source": "0627952d-ad4c-44d2-a32c-03baeca15215", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'date_of', 'label': 'Date Of', 'columnType': 'field', '_expanded': False}, {'field': 'City', 'label': 'City', 'columnType': 'lookup', 'lookupEntity': '3c4c6ca2-534b-472a-a05c-2b1a42fc3f5c', 'lookupField': 'City', '_expanded': False}], "id": "table-person-0", "filter": ""}
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
iypbf = ViewContainer(
    name="iypbf",
    description="main container",
    view_elements={ijaar, ikb2n, table_person_0},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="iypbf",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "iypbf"}
)
iypbf_layout = Layout(flex="1")
iypbf.layout = iypbf_layout
is13x = ViewContainer(
    name="is13x",
    description=" component",
    view_elements={i8d4f, iypbf},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="is13x",
    display_order=0,
    custom_attributes={"id": "is13x"}
)
is13x_layout = Layout(layout_type=LayoutType.FLEX)
is13x.layout = is13x_layout
wrapper.view_elements = {is13x}


# Screen: wrapper_2
wrapper_2 = Screen(name="wrapper_2", description="City", view_elements=set(), route_path="/city", screen_size="Medium")
wrapper_2.component_id = "page-city-1"
itwho = Text(
    name="itwho",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="itwho",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "itwho"}
)
imcp2 = Link(
    name="imcp2",
    description="Link element",
    label="Person",
    url="/person",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="imcp2",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/person", "id": "imcp2"}
)
i66ew = Link(
    name="i66ew",
    description="Link element",
    label="City",
    url="/city",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i66ew",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/city", "id": "i66ew"}
)
i9zih = ViewContainer(
    name="i9zih",
    description=" component",
    view_elements={imcp2, i66ew},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i9zih",
    display_order=1,
    custom_attributes={"id": "i9zih"}
)
i9zih_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i9zih.layout = i9zih_layout
ikdsh = Text(
    name="ikdsh",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="ikdsh",
    display_order=2,
    custom_attributes={"id": "ikdsh"}
)
iugo8 = ViewContainer(
    name="iugo8",
    description="nav container",
    view_elements={itwho, i9zih, ikdsh},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iugo8",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iugo8"}
)
iugo8_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iugo8.layout = iugo8_layout
ihbdj = Text(
    name="ihbdj",
    content="City",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ihbdj",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ihbdj"}
)
ihkns = Text(
    name="ihkns",
    content="Manage City data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ihkns",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ihkns"}
)
table_city_1_col_0 = FieldColumn(label="City", field=City_City)
table_city_1 = Table(
    name="table_city_1",
    title="City List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_city_1_col_0],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-city-1",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "City List", "data-source": "3c4c6ca2-534b-472a-a05c-2b1a42fc3f5c", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'City', 'label': 'City', 'columnType': 'field', '_expanded': False}, {'field': 'Person', 'label': 'Person', 'columnType': 'lookup', 'lookupEntity': '0627952d-ad4c-44d2-a32c-03baeca15215', 'lookupField': 'name', '_expanded': False}], "id": "table-city-1", "filter": ""}
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
is6sa = ViewContainer(
    name="is6sa",
    description="main container",
    view_elements={ihbdj, ihkns, table_city_1},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="is6sa",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "is6sa"}
)
is6sa_layout = Layout(flex="1")
is6sa.layout = is6sa_layout
i3ng5 = ViewContainer(
    name="i3ng5",
    description=" component",
    view_elements={iugo8, is6sa},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i3ng5",
    display_order=0,
    custom_attributes={"id": "i3ng5"}
)
i3ng5_layout = Layout(layout_type=LayoutType.FLEX)
i3ng5.layout = i3ng5_layout
wrapper_2.view_elements = {i3ng5}

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
