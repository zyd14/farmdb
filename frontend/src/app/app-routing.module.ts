import { NgModule } from '@angular/core';
import { PlanttypesComponent } from "./planttypes/planttypes.component";
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {path: 'plants', component: PlanttypesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
