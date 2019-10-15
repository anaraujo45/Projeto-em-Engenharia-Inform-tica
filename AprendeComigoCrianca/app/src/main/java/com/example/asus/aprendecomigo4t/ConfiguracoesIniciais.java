package com.example.asus.aprendecomigo4t;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class ConfiguracoesIniciais extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_configuracoes_iniciais);
    }

    public void ConfiguracoesBemVindo (View view){
        Intent it= new Intent(ConfiguracoesIniciais.this,Bem_Vindo_1.class);
        startActivity(it);
    }
}
