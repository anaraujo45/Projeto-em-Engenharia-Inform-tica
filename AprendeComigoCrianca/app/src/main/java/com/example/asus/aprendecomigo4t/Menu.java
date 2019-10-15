package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Menu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
    }

    public void OpcaoMatematica1a(View view){
        Intent it = new Intent(Menu.this, Matematica_1ano_Automatica.class);
        startActivity(it);
    }

    public void OpcaoPortugues1a(View view){
        Intent it = new Intent(Menu.this, Portugues_2ano_automatica.class);
        startActivity(it);
    }

    public void OpcaoEDM1a(View view){
        Intent it = new Intent(Menu.this,Estudo_do_Meio_1ano_automaticas.class);
        startActivity(it);
    }
}
