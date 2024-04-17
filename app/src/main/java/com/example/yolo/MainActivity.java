package com.example.yolo;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
     RadioGroup radioGroup;
     RadioButton radioButtonUser, radioButtonHospital;
     Button buttonLogin;
     Animation topAnim, bottomAnim;
     ImageView image;
     TextView logo, slogan;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        radioGroup = findViewById(R.id.radioGroup);
        radioButtonUser = findViewById(R.id.radioButton_user);
        radioButtonHospital = findViewById(R.id.radioButton_hospital);
        buttonLogin = findViewById(R.id.button_login);

        topAnim = AnimationUtils.loadAnimation(this, R.anim.top_animation);
        bottomAnim = AnimationUtils.loadAnimation(this, R.anim.bottom_animation);

        image = findViewById(R.id.imageView);
        logo = findViewById(R.id.textView3);
        slogan = findViewById(R.id.textView4);

        image.setAnimation(topAnim);
        logo.setAnimation(bottomAnim);
        slogan.setAnimation(bottomAnim);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }
    public void onLoginClicked(View view) {
        int selectedId = radioGroup.getCheckedRadioButtonId();

        if (selectedId == -1) {
            Toast.makeText(MainActivity.this, "Please select User or Hospital", Toast.LENGTH_SHORT).show();
        } else {
            RadioButton selectedRadioButton = findViewById(selectedId);
            String loginAs = selectedRadioButton.getText().toString();

            if (loginAs.equals("User")) {
                Intent intent = new Intent(MainActivity.this, UserLoginActivity2.class);
                startActivity(intent);
            } else if (loginAs.equals("Hospital")) {
                Intent intent = new Intent(MainActivity.this, HospitalLoginActivity2.class);
                startActivity(intent);
            }
        }
    }
}