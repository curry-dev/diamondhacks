import { Component } from '@angular/core';
import { FormControl, FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-plantrip',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    FormsModule,
    CommonModule
  ],
  templateUrl: './plantrip.component.html',
  styleUrl: './plantrip.component.css'
})

export class PlantripComponent {
  whereto = new FormControl('');
  budget = new FormControl('');
  numpeople = new FormControl('');

  constructor(private _apiservice: ApiService) {}

  getTrip() {

  }
}
