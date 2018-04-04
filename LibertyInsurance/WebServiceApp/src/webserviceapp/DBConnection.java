package webserviceapp;

import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.Random;

public class DBConnection {

    private static final String DB_DRIVER = "oracle.jdbc.driver.OracleDriver";
    private static String DB_CONNECTION = "";
    private static final String DB_USER = "stateinsurance";
    private static final String DB_PASSWORD = "STateinsurance12@_";
    private static final int Big_Number = 500000000;
    
    public DBConnection(String IP, String SID) {
        DBConnection.DB_CONNECTION = "jdbc:oracle:thin:@"+IP+":1521:"+SID;
    }

    public void insertRecord(String v0, String v1, String v2, String v3) throws SQLException {

        Connection dbConnection = null;
        PreparedStatement statement = null;
        Random rand = new Random();
        int  n = rand.nextInt(Big_Number) + 1;
        
        System.out.println("before sql statement");
        
        Date exp = new Date();
        int noOfDays = 14; //i.e two weeks
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(exp);            
        calendar.add(Calendar.DAY_OF_YEAR, noOfDays);
        Date date = calendar.getTime();
        
        java.sql.Date sqlDate = new java.sql.Date(date.getTime());
        
        String insertTableSQL = "INSERT INTO insurance (policy, name, address, phone, ssn, company, exp) VALUES ("
                + "?, ?, ?, ?, ?, ?, ?)";
                                

        try {
            dbConnection = getDBConnection();
            statement = dbConnection.prepareStatement(insertTableSQL);
            statement.setInt(1, n);
            statement.setString(2, v0);
            statement.setString(3, v1);
            statement.setString(4, v2);
            statement.setString(5, v3);
            statement.setString(6, "Liberty Insurance");
            statement.setDate(7, sqlDate);
            
            // execute insert SQL stetement
            statement.executeUpdate();

            System.out.println("Record is inserted into table!");

        } catch (SQLException e) {

            System.out.println(e.getMessage());

        } finally {

            if (statement != null) {
                statement.close();
            }

            if (dbConnection != null) {
                dbConnection.close();
            }

        }

    }
    
    public ArrayList selectAll() throws SQLException {

        Connection dbConnection = null;
        Statement statement = null;

        String selectSQL = "SELECT * FROM insurance";
        
        System.out.println(selectSQL);

        try {
            dbConnection = getDBConnection();
            statement = dbConnection.createStatement();

            System.out.println("Table is selected!");
            
            ResultSet rs = statement.executeQuery(selectSQL);
            
            ArrayList<String> customers = new ArrayList<String>(); 
            while (rs.next()) {
                String name = rs.getString("NAME");
                String policy = rs.getString("POLICY");
                String address = rs.getString("ADDRESS");
                String phone = rs.getString("PHONE");
                String ssn = rs.getString("SSN");
                String company = rs.getString("COMPANY");
                Date exp = rs.getTimestamp("EXP");
                String object = "{\"name\": \""+name+"\", \"address\": \""+address+"\", \"phone\": \""+phone+"\"" +
                    ", \"ssn\": \""+ssn+"\", \"policy\": \""+policy+"\", \"company\": \""+company+"\", \"exp\": \""+exp+"\"}";
                customers.add(object);
            }
            return customers; 
            
        } catch (SQLException e) {

            System.out.println(e.getMessage());

        } finally {

            if (statement != null) {
                statement.close();
            }

            if (dbConnection != null) {
                dbConnection.close();
            }

        } return new ArrayList<String>();

    }

    private static Connection getDBConnection() {

        Connection dbConnection = null;

        try {

            Class.forName(DB_DRIVER);

        } catch (ClassNotFoundException e) {

            System.out.println(e.getMessage());

        }

        try {
            System.out.println("before connecting to database" + DB_CONNECTION + " " + DB_USER + " " + DB_PASSWORD);
            
            dbConnection = DriverManager.getConnection(
                    DB_CONNECTION, DB_USER, DB_PASSWORD);
            return dbConnection;

        } catch (SQLException e) {

            System.out.println(e.getMessage());

        }

        return dbConnection;

    }
    
////     TEST Main
//    public static void main(String[] argv) {
//
//        try {
//
////            insertRecord("hello2", "heya", "pppp", ";lkj");
//            System.out.println(selectAll());
//
//        } catch (SQLException e) {
//
//            System.out.println(e.getMessage());
//
//        }
//
//    }


}
