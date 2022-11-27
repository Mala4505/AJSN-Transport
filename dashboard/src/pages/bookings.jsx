import React, { useState, useEffect } from "react";

import { Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../theme";
import Header from "../components/Header";
import { useTheme } from "@mui/material";



const Bookings = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [driver, setDriver] = useState([]);

  useEffect(() => {
    const setdriver = async () => {
      const res = await fetch("http://127.0.0.1:8000/administration/bookings/");
      const getdata = await res.json();
      setDriver(getdata);
      // console.log(getdata);
    };
    setdriver();
  },[]);

  const columns = [
    { field: "CB_Trans_Id", headerName: "ID", flex: 0.5 },
    {
      field: "UserId",
      headerName: "Username",
      cellClassName: "name-column--cell",
    },
    {
      field: "CB_For_ID",
      headerName: "Option",
      flex: 0.5,
    },
    {
      field: "Source",
      headerName: "Source",
    },
    {
      field: "Destination",
      headerName: "Destination",
    },
    {
      field: "No_Of_Passenger",
      headerName: "Passengers",
      flex: '0.5'
    },
    {
      field: "Purpose",
      headerName: "Purpose",
    },
    {
      field: "Time_From",
      headerName: "From",
    },
    {
      field: "Time_To",
      headerName: "To",
    },
    {
      field: "Actual_Time_To",
      headerName: "Actual Time",
    },
    {
      field: "CBStatus",
      headerName: "CBStatus",
    },
    {
      field: "CarId",
      headerName: "Car ID",
    },
    {
      field: "Driver_ID",
      headerName: "Driver ID",
    },
    {
      field: "StartKm",
      headerName: "Start KM",
    },
    {
      field: "EndKm",
      headerName: "End KM",
    },
    {
      field: "TotalKmTravelled",
      headerName: "Total KM",
    },
    {
      field: "Estimated_Amt",
      headerName: "Estimated AMT",
    },
    {
      field: "Actual_Amt",
      headerName: "Actual AMT",
    },
    {
      field: "Payment_Ref_Id",
      headerName: "Payment Type",
    },
    {
      field: "Payment_Status",
      headerName: "Payment Status",
    },
    {
      field: "Submitted_By",
      headerName: "Submitted By",
    },
    {
      field: "Overtime",
      headerName: "Overtime",
    },
    {
      field: "Overtime_Time",
      headerName: "Overtime_Time",
    },
    {
      field: "TimeStamp",
      headerName: "TimeStamp",
    },

  ];

  return (
    <Box m="20px" p="2rem" height="100%">
      <Header
        title="Bookings"
        subtitle="List of Bookings"
      />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
          "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
          },
        }}
      >
        <DataGrid
          checkboxSelection
          rows={driver}
          columns={columns}
          getRowId={(row) => row.CB_Trans_Id}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>
    </Box>
  );
};

export default Bookings;